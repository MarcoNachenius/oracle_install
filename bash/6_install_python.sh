#!/usr/bin/bash

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  CONFIGURABLE CONSTANTS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# =====================
# CONFIGURABLE SETTINGS
# =====================
# Python version to install (3.11, 3.12, etc. - use 'latest' for system default)
readonly PYTHON_VERSION="3.12"
# Path to requirements.txt file (path from inside the repository)
readonly REQUIREMENTS_FILE_DIR="python/requirements.txt"
# ==========
# EXIT CODES
# ==========
readonly GENERAL_ERROR_EXIT_CODE=1

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  HELPER FUNCTIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
# Purpose:  Terminate script execution immediately with an error message and
#           non-zero exit status.
#
# Behavior: - Prints formatted error message to STDERR (not STDOUT)
#           - Ensures errors are visible even when output is redirected
#           - Exits script with status code 1 (general error exit code)
#           - Supports dynamic error messages via function arguments
#
# Usage:    die "Database connection failed"
#           die "File not found: ${filename}"
#           die "Expected 2 arguments, got $#"
# ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
die() {
    # All die print messages contain '[ERROR]' as a prefix.
    #
    # Why $* instead of $1?
    # - Flexibility: Allows callers to pass multiple arguments that get automatically
    #   concatenated into a single error message.
    # - Natural syntax: die "File" $filename "not found" works without
    #   manual string concatenation or quoting.
    # - Future-proof: Accommodates complex error messages that might need to
    #   combine literals and variables naturally.
    #
    # The '>&2' syntax redirects output from STDOUT (file descriptor 1)
    # to STDERR (file descriptor 2). This ensures error messages are
    # properly separated from normal program output streams.
    echo "[ERROR] $*" >&2
    
    # Exit with relevant code
    exit $GENERAL_ERROR_EXIT_CODE
}

print_info() {
    echo "[INFO] $*"
}

print_success() {
    echo "[SUCCESS] $*"
}

print_warning() {
    echo "[WARNING] $*"
}

# ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
# Purpose: Install Python using dnf package manager
# ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
install_python_with_dnf() {
    print_info "Installing Python using dnf package manager..."
    
    # Try to install the specific version
    if sudo dnf install -y "python${PYTHON_VERSION}" "python${PYTHON_VERSION}-pip" 2>/dev/null; then
        print_success "Python ${PYTHON_VERSION} installed successfully"
    fi
}


# ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
# Purpose: Create and activate a Python virtual environment
# ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●


# ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
# Purpose: Install Python packages from requirements.txt
# ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
install_requirements() {
    if [[ ! -f "$REQUIREMENTS_FILE_DIR" ]]; then
        print_warning "Requirements file not found: $REQUIREMENTS_FILE_DIR"
        print_info "Skipping package installation"
        return 0
    fi
    
    print_info "Installing packages from: $REQUIREMENTS_FILE_DIR"
    
    # Handle potential slow network or repository issues with retries
    # --timeout: Maximum time (in seconds) to wait for a response from the server
    # --retries: Number of times to retry in case of failure
    # --no-cache-dir: Avoid using cached packages to ensure fresh downloads
    "pip${PYTHON_VERSION}" install -r "${REQUIREMENTS_FILE_DIR}"
    
    print_success "All Python packages installed successfully"
}


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  MAIN EXECUTION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
main() {
    print_info "Starting Python installation..."
    print_info "Configuration:"
    print_info "  Python Version: $PYTHON_VERSION"
    print_info "  Requirements File: $REQUIREMENTS_FILE_DIR"
    
    # Install Python
    install_python_with_dnf || die "Failed to install Python"
    # Install requirements
    install_requirements || die "Failed to install Python requirements"
}


# Run the main function
main || die "Python installation script failed unexpectedly."