# =============================================================================
# CONFIGURATION MODULE
# This module stores all the file extension definitions used throughout
# the analyzer. By keeping them in one place, it's easy to add support
# for new file types later.
# =============================================================================

# -----------------------------------------------------------------------------
# CONFIGURATION FILE EXTENSIONS
# These are the file extensions we treat as "configuration files".
# When a file with one of these extensions changes, we know we need to
# parse it differently from source code files.
# -----------------------------------------------------------------------------
CONFIG_EXTENSIONS = {
    "yml",          # YAML files (used by Kubernetes, Docker Compose, etc.)
    "yaml",         # YAML files (alternative extension)
    "properties",   # Java properties files
    "json",         # JSON configuration files
    "xml",          # XML configuration files
}

# -----------------------------------------------------------------------------
# SOURCE CODE FILE EXTENSIONS
# These are the file extensions we treat as "source code files".
# When a file with one of these extensions changes, we extract words
# from it and compare with words in test files.
# -----------------------------------------------------------------------------
SOURCE_EXTENSIONS = {
    "py",           # Python files
    "java",         # Java files
    "js",           # JavaScript files
    "ts",           # TypeScript files
    "cpp",          # C++ source files
    "c",            # C source files
    "cs",           # C# files
    "go",           # Go files
    "rb",           # Ruby files
    "php",          # PHP files
}

# -----------------------------------------------------------------------------
# TEST FILE PATTERNS
# These patterns help us identify which files are test files.
# A file is considered a test file if its name contains any of these patterns.
# -----------------------------------------------------------------------------
TEST_FILE_PATTERNS = {
    "test_",        # Example: test_order_service.py
    "_test",        # Example: order_service_test.py
    "Test",         # Example: OrderServiceTest.java
    "spec",         # Example: order_service_spec.js
}