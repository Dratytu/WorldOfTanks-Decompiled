@echo off

REM Prevents the command prompt from displaying most of the commands as they are run

echo.
echo Searching and deleting directories:
echo.

set "source=%~dp0source\res"

REM Sets the source directory to the "res" directory inside the directory where the batch script is located

for /f "tokens=* delims=" %%d in ('dir /ad/b/ON "%source%" 2^>nul') do (
    REM Loops through all directories in the source directory

    for %%x in (gui vscript) do (
        REM Loops through the "gui" and "vscript" directories inside each directory in the source directory

        set "directory=%source%\%%d\%%x"

        if exist "!directory!" (
            REM Checks if the "gui" or "vscript" directory exists inside the current directory

            del "!directory!\*.*" /s/f/q >nul 2^>nul
            REM Deletes all files inside the "gui" or "vscript" directory and its subdirectories quietly (without prompts)

            cd /d "!source!\%%d"
            REM Changes the current directory to the parent directory of the "gui" or "vscript" directory

            rd "!directory!" /s/q >nul 2^>nul
            REM Deletes the "gui" or "vscript" directory and its contents quietly (without prompts)

            echo     !directory!
            REM Echos the path of the deleted "gui" or "vscript" directory for the user to see

        )
    )
)

echo.
pause

REM Pauses the script to allow the user to see the output before the console window closes
