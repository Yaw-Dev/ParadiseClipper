@echo off

pip install pyperclip
cls

:givename
color 0a
echo.
set /p a="Enter the exe name: "
if [%a%]==[] ( 
    cls
    echo.
    color 0c
    echo Error: Invalid or no name was given.
    pause
    cls
    goto givename
) 
if [%a%] NEQ [] (
    echo.
    echo Name is: %a%
    pyinstaller --noconfirm --onefile --windowed --icon "NONE" --hidden-import "pyperclip" -n %a% clipper.py
    rmdir /s /q __pycache__
    rmdir /s /q build
    del /f / s /q %a%.spec
    echo.
    echo Generated exe as %a%.exe in the dist folder
    echo.
    pause
    EXIT /B 1
)