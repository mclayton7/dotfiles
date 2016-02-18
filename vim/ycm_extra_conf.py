################################################################################
#
# Mac Clayton 2015
#
# This is a configuration file for Vim's YouCompleteMe plugin to work with
# clang's completion engine. For this to work correctly, a JSON compilation
# database must be generated. The compilation_database_folder variable must
# point to the FOLDER of the database. The filename will be
# compile_commands.json.
#
# For waf this is done with waf's clang_compilation_database.py tool and the
# flag --with-json-database.
#
# For more information:
# https://github.com/Valloric/ycmd/blob/master/cpp/ycm/.ycm_extra_conf.py
# https://github.com/waf-project/waf/blob/master/waflib/extras/clang_compilation_database.py
# http://clang.llvm.org/docs/JSONCompilationDatabase.html
#
################################################################################

import os
import ycm_core


def compilationDatabaseFolder():
      return "folder"


compilation_database_folder = compilationDatabaseFolder()

if os.path.exists(compilation_database_folder):
   database = ycm_core.CompilationDatabase(compilation_database_folder)
else:
   database = None

SOURCE_EXTENSIONS = ['.cxx']


def MakeRelativePathsInFlagsAbsolute(flags, working_directory):
   if not working_directory:
      return list(flags)
   new_flags = []
   make_next_absolute = False
   path_flags = [ '-isystem', '-I', '-iquote', '--sysroot=']
   for flag in flags:
      new_flag = flag

      if make_next_absolute:
         make_next_absolute = False
         if not flag.startswith('/'):
            new_flag = os.path.join(working_directory, flag)

      for path_flag in path_flags:
         if flag == path_flag:
            make_next_absolute = True
            break

         if flag.startswith(path_flag):
            path = flag[ len(path_flag):]
            new_flag = path_flag + os.path.join(working_directory, path)
            break

      if new_flag:
         new_flags.append(new_flag)
   return new_flags


def IsHeaderFile(filename):
   extension = os.path.splitext(filename)[ 1]
   return extension in ['.h']


def GetCompilationInfoForFile(filename):
   # The compilation_commands.json file generated by CMake/Waf does not have entries
   # for header files. So we do our best by asking the db for flags for a
   # corresponding source file, if any. If one exists, the flags for that file
   # should be good enough.
   if IsHeaderFile(filename):
      basename = os.path.splitext(filename)[ 0]
      for extension in SOURCE_EXTENSIONS:
         replacement_file = basename + extension
         if os.path.exists(replacement_file):
            compilation_info = database.GetCompilationInfoForFile(
               replacement_file)
            if compilation_info.compiler_flags_:
               return compilation_info
      return None
   return database.GetCompilationInfoForFile(filename)


def FlagsForFile(filename, **kwargs):
   if database:
      # Bear in mind that compilation_info.compiler_flags_ does NOT return a
      # python list, but a "list-like" StringVec object
      compilation_info = GetCompilationInfoForFile(filename)
      if not compilation_info:
         return None

      final_flags = MakeRelativePathsInFlagsAbsolute(
         compilation_info.compiler_flags_,
         compilation_info.compiler_working_dir_)

   else:
      raise IOError('File not found')

   return {
      'flags': final_flags,
      'do_cache': True
   }
