@echo off
setlocal enabledelayedexpansion
set SPHINXBUILD=..\.venv\Scripts\sphinx-build.exe
set SOURCEDIR=.
set BUILDDIR=_build
if "%1"=="clean" (
    rd /s /q %BUILDDIR%
    exit /b 0
)
%SPHINXBUILD% -M html "%SOURCEDIR%" "%BUILDDIR%" -q
