@ECHO off

:: VARIABLES
SET ECHO_NL=^&ECHO:
SET python_version_min=3.7.0
SET pygame_version_min=1.9.4
SET main_location=main.py
SET error_no_main=Missing files... Try to download the game again.
SET error_no_python=Python not found. You need to install it first!
SET error_wrong_python_version=Wrong python version...
SET error_no_pygame=Pygame not found. Trying to install...
SET error_wrong_pygame_version=Wrong pygame version. Trying to update...

:: CHECK FOR FILES (just main file for now)
IF NOT EXIST %main_location% (
	ECHO %error_no_main% %ECHO_NL%
	GOTO END
)

:: CHECK IF PYTHON IS INSTALLED
ECHO Checking for python...
FOR /F "tokens=* USEBACKQ" %%G IN (`"py --version"`) DO (SET helper=%%G)
:: check if `py --version` returned anything - can't use FINDSTR (...is not recognized as... error returns empty string)
IF "%helper%" == "" (
	ECHO %error_no_python% %ECHO_NL%
	GOTO END
)
:: check python version
CALL SET python_version=%helper:Python =%
SET python_version_int=%python_version:.=%
SET python_version_min_int=%python_version_min:.=%
IF %python_version_int% LSS %python_version_min_int% (
	ECHO %error_wrong_python_version% (have %python_version%, minimal %python_version_min%^)
	GOTO END
)
ECHO Python found! (%python_version%) %ECHO_NL%

:: CHECK IF PYGAME IS INSTALLED
ECHO Checking for needed libraries...
FOR /F "tokens=* USEBACKQ" %%G IN (`"py -m pip freeze | findstr pygame"`) DO (SET helper=%%G)
:: check if `"py -m pip freeze | findstr pygame"` returned appropriate data
ECHO %helper% | FINDSTR /C:"pygame==" || (
	ECHO %error_no_pygame% %ECHO_NL%
	py -m pip install pygame
	:: update helper with new version
	FOR /F "tokens=* USEBACKQ" %%G IN (`"py -m pip freeze | findstr pygame"`) DO (SET helper=%%G)
)
:: check pygame version
CALL SET pygame_version_with_equals=%helper:pygame=%
SET pygame_version=%pygame_version_with_equals:~2%
SET pygame_version_int=%pygame_version:.=%
SET pygame_version_min_int=%pygame_version_min:.=%
IF %pygame_version_int% LSS %pygame_version_min_int% (
	ECHO %error_wrong_pygame_version% (have %pygame_version%, minimal %pygame_version_min%^)
	py -m pip install --upgrade pygame
)
ECHO Everything should be fine! Have fun! %ECHO_NL%

:: RUN GAME
py %main_location% >nul

:: END BLOCK
:END
PAUSE