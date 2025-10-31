#!/usr/bin/bash

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  CONSTANTS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
readonly PYTHON_DIR="python"
readonly VENV_DIR="${PYTHON_DIR}/.venv"
readonly MAIN_SCRIPT="main.py"
readonly GENERAL_ERROR_EXIT_CODE=1

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  HELPER FUNCTIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
die() {
    echo "[ERROR] $*" >&2
    exit $GENERAL_ERROR_EXIT_CODE
}

print_info() {
    echo "[INFO] $*"
}

print_success() {
    echo "[SUCCESS] $*"
}

# ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
# Purpose: Activate virtual environment and run the main Python script
# ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
run_python_app() {
    print_info "Starting DB writer..."
    
    # Check if python directory exists
    if [[ ! -d "$PYTHON_DIR" ]]; then
        die "Python directory not found: $PYTHON_DIR"
    fi
    
    # Check if virtual environment exists
    if [[ ! -d "$VENV_DIR" ]]; then
        die "Virtual environment not found. Please run the setup script first: $VENV_DIR"
    fi
    
    # Check if main.py exists
    if [[ ! -f "${PYTHON_DIR}/${MAIN_SCRIPT}" ]]; then
        die "Main script not found: ${PYTHON_DIR}/${MAIN_SCRIPT}"
    fi
    
    # Change to python directory
    cd "$PYTHON_DIR" || die "Failed to change directory to: $PYTHON_DIR"
    
    # Activate virtual environment
    print_info "Activating virtual environment..."
    source "${VENV_DIR}/bin/activate" || die "Failed to activate virtual environment"
    
    # Verify activation
    if [[ -z "$VIRTUAL_ENV" ]]; then
        die "Virtual environment activation failed"
    fi
    
    print_success "Virtual environment activated: $VIRTUAL_ENV"
    
    # Run the main Python script
    print_info "Running main.py..."
    python "$MAIN_SCRIPT"
    
    # Capture the exit code
    local exit_code=$?
    
    # Deactivate virtual environment
    deactivate 2>/dev/null
    
    # Return to original directory
    cd - > /dev/null || print_info "Returned to original directory"
    
    # Return the exit code from the Python script
    return $exit_code
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  MAIN EXECUTION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
main() {
    print_info "Launching DB writer..."
    run_python_app
}

# Run the main function
main