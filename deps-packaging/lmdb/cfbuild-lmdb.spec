Source0: 14cff072ec29f48093a9d40cc79934cf5376af4a.tar.gz
%define srcdir lmdb-14cff072ec29f48093a9d40cc79934cf5376af4a/libraries/liblmdb
# Workaround for automake being sensitive to the order in which the generated
# files are applied. If Makefile.in is patched before aclocal.m4 (which it is,
# following natural file order), then it will try to rebuild Makefile.in, which
# it can't without automake. Work around it by touching that file.
touch Makefile.in
