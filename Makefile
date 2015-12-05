# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.4

# Default target executed when no arguments are given to make.
default_target: all

.PHONY : default_target

# Allow only one "make -f Makefile2" at a time, but pass parallelism.
.NOTPARALLEL:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/bin/cmake

# The command to remove a file.
RM = /usr/local/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/user/Desktop/QServ/cp

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/user/Desktop/QServ/cp

#=============================================================================
# Targets provided globally by CMake.

# Special rule for the target list_install_components
list_install_components:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "Available install components are: \"Unspecified\""
.PHONY : list_install_components

# Special rule for the target list_install_components
list_install_components/fast: list_install_components

.PHONY : list_install_components/fast

# Special rule for the target install
install: preinstall
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "Install the project..."
	/usr/local/bin/cmake -P cmake_install.cmake
.PHONY : install

# Special rule for the target install
install/fast: preinstall/fast
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "Install the project..."
	/usr/local/bin/cmake -P cmake_install.cmake
.PHONY : install/fast

# Special rule for the target install/local
install/local: preinstall
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "Installing only the local directory..."
	/usr/local/bin/cmake -DCMAKE_INSTALL_LOCAL_ONLY=1 -P cmake_install.cmake
.PHONY : install/local

# Special rule for the target install/local
install/local/fast: install/local

.PHONY : install/local/fast

# Special rule for the target rebuild_cache
rebuild_cache:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "Running CMake to regenerate build system..."
	/usr/local/bin/cmake -H$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR)
.PHONY : rebuild_cache

# Special rule for the target rebuild_cache
rebuild_cache/fast: rebuild_cache

.PHONY : rebuild_cache/fast

# Special rule for the target edit_cache
edit_cache:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --cyan "Running CMake cache editor..."
	/usr/local/bin/ccmake -H$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR)
.PHONY : edit_cache

# Special rule for the target edit_cache
edit_cache/fast: edit_cache

.PHONY : edit_cache/fast

# The main all target
all: cmake_check_build_system
	$(CMAKE_COMMAND) -E cmake_progress_start /Users/user/Desktop/QServ/cp/CMakeFiles /Users/user/Desktop/QServ/cp/CMakeFiles/progress.marks
	$(MAKE) -f CMakeFiles/Makefile2 all
	$(CMAKE_COMMAND) -E cmake_progress_start /Users/user/Desktop/QServ/cp/CMakeFiles 0
.PHONY : all

# The main clean target
clean:
	$(MAKE) -f CMakeFiles/Makefile2 clean
.PHONY : clean

# The main clean target
clean/fast: clean

.PHONY : clean/fast

# Prepare targets for installation.
preinstall: all
	$(MAKE) -f CMakeFiles/Makefile2 preinstall
.PHONY : preinstall

# Prepare targets for installation.
preinstall/fast:
	$(MAKE) -f CMakeFiles/Makefile2 preinstall
.PHONY : preinstall/fast

# clear depends
depend:
	$(CMAKE_COMMAND) -H$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR) --check-build-system CMakeFiles/Makefile.cmake 1
.PHONY : depend

#=============================================================================
# Target rules for targets named qserv

# Build rule for target.
qserv: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 qserv
.PHONY : qserv

# fast build rule for target.
qserv/fast:
	$(MAKE) -f CMakeFiles/qserv.dir/build.make CMakeFiles/qserv.dir/build
.PHONY : qserv/fast

#=============================================================================
# Target rules for targets named enet

# Build rule for target.
enet: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 enet
.PHONY : enet

# fast build rule for target.
enet/fast:
	$(MAKE) -f enet/CMakeFiles/enet.dir/build.make enet/CMakeFiles/enet.dir/build
.PHONY : enet/fast

#=============================================================================
# Target rules for targets named GeoIP

# Build rule for target.
GeoIP: cmake_check_build_system
	$(MAKE) -f CMakeFiles/Makefile2 GeoIP
.PHONY : GeoIP

# fast build rule for target.
GeoIP/fast:
	$(MAKE) -f GeoIP/CMakeFiles/GeoIP.dir/build.make GeoIP/CMakeFiles/GeoIP.dir/build
.PHONY : GeoIP/fast

QCom.o: QCom.cpp.o

.PHONY : QCom.o

# target to build an object file
QCom.cpp.o:
	$(MAKE) -f CMakeFiles/qserv.dir/build.make CMakeFiles/qserv.dir/QCom.cpp.o
.PHONY : QCom.cpp.o

QCom.i: QCom.cpp.i

.PHONY : QCom.i

# target to preprocess a source file
QCom.cpp.i:
	$(MAKE) -f CMakeFiles/qserv.dir/build.make CMakeFiles/qserv.dir/QCom.cpp.i
.PHONY : QCom.cpp.i

QCom.s: QCom.cpp.s

.PHONY : QCom.s

# target to generate assembly for a file
QCom.cpp.s:
	$(MAKE) -f CMakeFiles/qserv.dir/build.make CMakeFiles/qserv.dir/QCom.cpp.s
.PHONY : QCom.cpp.s

QServ.o: QServ.cpp.o

.PHONY : QServ.o

# target to build an object file
QServ.cpp.o:
	$(MAKE) -f CMakeFiles/qserv.dir/build.make CMakeFiles/qserv.dir/QServ.cpp.o
.PHONY : QServ.cpp.o

QServ.i: QServ.cpp.i

.PHONY : QServ.i

# target to preprocess a source file
QServ.cpp.i:
	$(MAKE) -f CMakeFiles/qserv.dir/build.make CMakeFiles/qserv.dir/QServ.cpp.i
.PHONY : QServ.cpp.i

QServ.s: QServ.cpp.s

.PHONY : QServ.s

# target to generate assembly for a file
QServ.cpp.s:
	$(MAKE) -f CMakeFiles/qserv.dir/build.make CMakeFiles/qserv.dir/QServ.cpp.s
.PHONY : QServ.cpp.s

engine/command.o: engine/command.cpp.o

.PHONY : engine/command.o

# target to build an object file
engine/command.cpp.o:
	$(MAKE) -f CMakeFiles/qserv.dir/build.make CMakeFiles/qserv.dir/engine/command.cpp.o
.PHONY : engine/command.cpp.o

engine/command.i: engine/command.cpp.i

.PHONY : engine/command.i

# target to preprocess a source file
engine/command.cpp.i:
	$(MAKE) -f CMakeFiles/qserv.dir/build.make CMakeFiles/qserv.dir/engine/command.cpp.i
.PHONY : engine/command.cpp.i

engine/command.s: engine/command.cpp.s

.PHONY : engine/command.s

# target to generate assembly for a file
engine/command.cpp.s:
	$(MAKE) -f CMakeFiles/qserv.dir/build.make CMakeFiles/qserv.dir/engine/command.cpp.s
.PHONY : engine/command.cpp.s

engine/server.o: engine/server.cpp.o

.PHONY : engine/server.o

# target to build an object file
engine/server.cpp.o:
	$(MAKE) -f CMakeFiles/qserv.dir/build.make CMakeFiles/qserv.dir/engine/server.cpp.o
.PHONY : engine/server.cpp.o

engine/server.i: engine/server.cpp.i

.PHONY : engine/server.i

# target to preprocess a source file
engine/server.cpp.i:
	$(MAKE) -f CMakeFiles/qserv.dir/build.make CMakeFiles/qserv.dir/engine/server.cpp.i
.PHONY : engine/server.cpp.i

engine/server.s: engine/server.cpp.s

.PHONY : engine/server.s

# target to generate assembly for a file
engine/server.cpp.s:
	$(MAKE) -f CMakeFiles/qserv.dir/build.make CMakeFiles/qserv.dir/engine/server.cpp.s
.PHONY : engine/server.cpp.s

fpsgame/server.o: fpsgame/server.cpp.o

.PHONY : fpsgame/server.o

# target to build an object file
fpsgame/server.cpp.o:
	$(MAKE) -f CMakeFiles/qserv.dir/build.make CMakeFiles/qserv.dir/fpsgame/server.cpp.o
.PHONY : fpsgame/server.cpp.o

fpsgame/server.i: fpsgame/server.cpp.i

.PHONY : fpsgame/server.i

# target to preprocess a source file
fpsgame/server.cpp.i:
	$(MAKE) -f CMakeFiles/qserv.dir/build.make CMakeFiles/qserv.dir/fpsgame/server.cpp.i
.PHONY : fpsgame/server.cpp.i

fpsgame/server.s: fpsgame/server.cpp.s

.PHONY : fpsgame/server.s

# target to generate assembly for a file
fpsgame/server.cpp.s:
	$(MAKE) -f CMakeFiles/qserv.dir/build.make CMakeFiles/qserv.dir/fpsgame/server.cpp.s
.PHONY : fpsgame/server.cpp.s

ircbot/ircbot.o: ircbot/ircbot.cpp.o

.PHONY : ircbot/ircbot.o

# target to build an object file
ircbot/ircbot.cpp.o:
	$(MAKE) -f CMakeFiles/qserv.dir/build.make CMakeFiles/qserv.dir/ircbot/ircbot.cpp.o
.PHONY : ircbot/ircbot.cpp.o

ircbot/ircbot.i: ircbot/ircbot.cpp.i

.PHONY : ircbot/ircbot.i

# target to preprocess a source file
ircbot/ircbot.cpp.i:
	$(MAKE) -f CMakeFiles/qserv.dir/build.make CMakeFiles/qserv.dir/ircbot/ircbot.cpp.i
.PHONY : ircbot/ircbot.cpp.i

ircbot/ircbot.s: ircbot/ircbot.cpp.s

.PHONY : ircbot/ircbot.s

# target to generate assembly for a file
ircbot/ircbot.cpp.s:
	$(MAKE) -f CMakeFiles/qserv.dir/build.make CMakeFiles/qserv.dir/ircbot/ircbot.cpp.s
.PHONY : ircbot/ircbot.cpp.s

shared/crypto.o: shared/crypto.cpp.o

.PHONY : shared/crypto.o

# target to build an object file
shared/crypto.cpp.o:
	$(MAKE) -f CMakeFiles/qserv.dir/build.make CMakeFiles/qserv.dir/shared/crypto.cpp.o
.PHONY : shared/crypto.cpp.o

shared/crypto.i: shared/crypto.cpp.i

.PHONY : shared/crypto.i

# target to preprocess a source file
shared/crypto.cpp.i:
	$(MAKE) -f CMakeFiles/qserv.dir/build.make CMakeFiles/qserv.dir/shared/crypto.cpp.i
.PHONY : shared/crypto.cpp.i

shared/crypto.s: shared/crypto.cpp.s

.PHONY : shared/crypto.s

# target to generate assembly for a file
shared/crypto.cpp.s:
	$(MAKE) -f CMakeFiles/qserv.dir/build.make CMakeFiles/qserv.dir/shared/crypto.cpp.s
.PHONY : shared/crypto.cpp.s

shared/stream.o: shared/stream.cpp.o

.PHONY : shared/stream.o

# target to build an object file
shared/stream.cpp.o:
	$(MAKE) -f CMakeFiles/qserv.dir/build.make CMakeFiles/qserv.dir/shared/stream.cpp.o
.PHONY : shared/stream.cpp.o

shared/stream.i: shared/stream.cpp.i

.PHONY : shared/stream.i

# target to preprocess a source file
shared/stream.cpp.i:
	$(MAKE) -f CMakeFiles/qserv.dir/build.make CMakeFiles/qserv.dir/shared/stream.cpp.i
.PHONY : shared/stream.cpp.i

shared/stream.s: shared/stream.cpp.s

.PHONY : shared/stream.s

# target to generate assembly for a file
shared/stream.cpp.s:
	$(MAKE) -f CMakeFiles/qserv.dir/build.make CMakeFiles/qserv.dir/shared/stream.cpp.s
.PHONY : shared/stream.cpp.s

shared/tools.o: shared/tools.cpp.o

.PHONY : shared/tools.o

# target to build an object file
shared/tools.cpp.o:
	$(MAKE) -f CMakeFiles/qserv.dir/build.make CMakeFiles/qserv.dir/shared/tools.cpp.o
.PHONY : shared/tools.cpp.o

shared/tools.i: shared/tools.cpp.i

.PHONY : shared/tools.i

# target to preprocess a source file
shared/tools.cpp.i:
	$(MAKE) -f CMakeFiles/qserv.dir/build.make CMakeFiles/qserv.dir/shared/tools.cpp.i
.PHONY : shared/tools.cpp.i

shared/tools.s: shared/tools.cpp.s

.PHONY : shared/tools.s

# target to generate assembly for a file
shared/tools.cpp.s:
	$(MAKE) -f CMakeFiles/qserv.dir/build.make CMakeFiles/qserv.dir/shared/tools.cpp.s
.PHONY : shared/tools.cpp.s

# Help Target
help:
	@echo "The following are some of the valid targets for this Makefile:"
	@echo "... all (the default if no target is provided)"
	@echo "... clean"
	@echo "... depend"
	@echo "... list_install_components"
	@echo "... install"
	@echo "... install/local"
	@echo "... rebuild_cache"
	@echo "... edit_cache"
	@echo "... qserv"
	@echo "... enet"
	@echo "... GeoIP"
	@echo "... QCom.o"
	@echo "... QCom.i"
	@echo "... QCom.s"
	@echo "... QServ.o"
	@echo "... QServ.i"
	@echo "... QServ.s"
	@echo "... engine/command.o"
	@echo "... engine/command.i"
	@echo "... engine/command.s"
	@echo "... engine/server.o"
	@echo "... engine/server.i"
	@echo "... engine/server.s"
	@echo "... fpsgame/server.o"
	@echo "... fpsgame/server.i"
	@echo "... fpsgame/server.s"
	@echo "... ircbot/ircbot.o"
	@echo "... ircbot/ircbot.i"
	@echo "... ircbot/ircbot.s"
	@echo "... shared/crypto.o"
	@echo "... shared/crypto.i"
	@echo "... shared/crypto.s"
	@echo "... shared/stream.o"
	@echo "... shared/stream.i"
	@echo "... shared/stream.s"
	@echo "... shared/tools.o"
	@echo "... shared/tools.i"
	@echo "... shared/tools.s"
.PHONY : help



#=============================================================================
# Special targets to cleanup operation of make.

# Special rule to run CMake to check the build system integrity.
# No rule that depends on this can have commands that come from listfiles
# because they might be regenerated.
cmake_check_build_system:
	$(CMAKE_COMMAND) -H$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR) --check-build-system CMakeFiles/Makefile.cmake 0
.PHONY : cmake_check_build_system

