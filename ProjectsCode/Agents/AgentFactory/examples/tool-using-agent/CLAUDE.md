# Code Analyzer Agent

An example agent that demonstrates file access capabilities - reading and analyzing code files.

## Overview

This agent can read files in a codebase to answer questions about the code, find patterns, and provide analysis. It demonstrates proper use of Read, Glob, and Grep tools.

## Purpose

Demonstrates an agent with file access:
- Uses Read, Glob, Grep tools
- Has specific directory permissions
- Includes file access in settings.json

## When to Use This Pattern

Use this pattern when your agent needs to:
- Read files from the filesystem
- Search for patterns in code
- Analyze existing content
- But NOT write or modify files

## File Access

This example assumes access to a hypothetical `/project` directory. When using this as a template, update the paths in settings.json to match your actual directory structure.
