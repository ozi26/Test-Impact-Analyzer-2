# Test Impact Analyzer for Microservice Applications

Hey there! 👋 This is a simple tool that helps you figure out which tests you need to run when you change your code or configuration files.

## What Does This Do?

Imagine you have a big application with lots of tests. Every time you change a tiny thing, you have to run ALL the tests. That takes forever! This tool helps you:

1. **See what changed** - It looks at your Git changes and figures out which files were modified
2. **Understand configuration files** - Unlike other tools, this one also looks at YAML, JSON, and other config files
3. **Find affected tests** - It tells you which tests are actually affected by your changes
4. **Save time** - You only run the tests you need to run!

## Why Is This Different?

Most test impact tools only look at source code changes. But in modern applications, changing a configuration file (like a timeout value) can break things too! This tool understands both.

## What You Need

- Python 3.10 or newer
- Git (for tracking changes)
- pip (for installing packages)

## Installation

1. **Clone or download this project**
   ```bash
   cd test-impact-analyzer