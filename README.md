## Prerequisites

Due to sheer diversity of the environments, build machine is expected to provide
strict minimum amount of software (don't forget --no-install-recommends on
dpkg-based systems):

To access the build machine:
 * SSH server
  * Bundled one on Unixes
  * FreeSSHd on Windows
 * 'build' account with SSH key installed

To transfer files back and forth:
 * rsync on Unixes
 * 7z on Windows

To be able to install packages and run tests:
 * passwordless sudo access for 'build' account
 * sudo should not require TTY (remove 'Defaults requiretty' from /etc/sudoers)

To build everything:
 * GCC (gcc)
 * GNU make (make)
 * libc development package (libc-dev, glibc-devel)
 * bison (bison)
 * flex (flex)
 * fakeroot (but not fakeroot 1.12, it is horribly slow!)

To create packages:
 * Native packaging manager
  * rpm-build on RPM-based systems
  * dpkg-dev, debhelper, fakeroot
  * WiX on Windows

To build MySQL library (yeah!):
 * g++ (gcc-c++, g++)
 * ncurses (ncurses-devel, libncurses5-dev)

To build libvirt:
 * pkg-config (pkg-config, pkgconfig)

Anything else is either preprocessed on buildbot slave or built and installed
during build.

## Documentation build pre-requisites

 * texinfo
 * texlive
 * cm-super
 * texlive-fonts-extra

## Non-requisites

Build machines should not contain the following items, which may interfere with
build process:

 * CFEngine itself, either in source or binary form (build machines are
   short-living, so this is not a problem)
 * Development packages for anything beside libc to avoid picking them up
   instead of bundled ones accidentally.
 * MySQL and PostgreSQL servers, clients and libraries

The following packages should not be installed on build machines as well, to
avoid accidentally regenerating files transferred from buildslave:

 * automake
 * autoconf
 * libtool

## Dependencies

File `install-dependencies` and the relevant subdirectories in `deps-packaging` are the source of this information.

### Build dependencies

| CFEngine version | 3.12.x | 3.15.x | master |
| ---------------- | ------ | ------ | ------ |
| lcov             | 1.14   | 1.14   | 1.14   |
| git              |        |        |        |
| rsync            |        |        |        |

### Agent Dependencies

| CFEngine version                                                                 | 3.12.x | 3.15.x | master | Notes                    |
| -------------------------------------------------------------------------------- | ------ | ------ | ------ | ------------------------ |
| [diffutils](https://ftpmirror.gnu.org/diffutils/)                                | -      | -      | 3.7    | Notes                    |
| [SASL2](https://cyrusimap.org/mediawiki/index.php/Downloads)                     | -      | -      | -      | Notes                    |
| [libacl](http://download.savannah.gnu.org/releases/acl/)                         | 2.2.53 | 2.2.53 | 2.2.53 | Notes                    |
| [libattr](http://download.savannah.gnu.org/releases/attr/)                       | 2.4.48 | 2.4.48 | 2.4.48 | Notes                    |
| [libcurl](http://curl.haxx.se/download.html)                                     | 7.72.0 | 7.72.0 | 7.73.0 | Notes                    |
| [libgnurx](http://www.gnu.org/software/rx/rx.html)                               | 2.5.1  | 2.5.1  | 2.5.1  | Notes                    |
| [libiconv](http://ftp.gnu.org/gnu/libiconv/)                                     | 1.16   | 1.16   | 1.16   | Notes                    |
| [libxml2](http://xmlsoft.org/sources/)                                           | 2.9.10 | 2.9.10 | 2.9.10 | Notes                    |
| [libyaml](http://pyyaml.org/wiki/LibYAML)                                        | 0.2.5  | 0.2.5  | 0.2.5  | Notes                    |
| [LMDB](https://github.com/LMDB/lmdb/)                                            | -      | -      | -      | Notes                    |
| [OpenLDAP](http://www.openldap.org/software/download/OpenLDAP/openldap-release/) | -      | -      | -      | Notes                    |
| [OpenSSL](http://openssl.org/)                                                   | -      | -      | -      | Notes                    |
| [PCRE](http://ftp.csx.cam.ac.uk/pub/software/programming/pcre/)                  | -      | -      | -      | Notes                    |
| [pthreads-w32](ftp://sourceware.org/pub/pthreads-win32/)                         | 2-9-1  | 2-9-1  | 2-9-1  | Notes                    |
| [zlib](http://www.zlib.net/)                                                     | 1.2.11 | 1.2.11 | 1.2.11 | Notes                    |
| libgcc                                                                           |        |        |        | AIX and Solaris only     |

### Enterprise Hub dependencies:

| CFEngine version                                    | 3.12.x | 3.15.x | master |
| --------------------------------------------------- | ------ | ------ | ------ |
| [Apache](http://httpd.apache.org/)                  | -      | -      | -      |
| [APR](https://apr.apache.org/)                      | -      | -      | -      |
| [apr-util](https://apr.apache.org/)                 | 1.6.1  | 1.6.1  | 1.6.1  |
| [Git](https://www.kernel.org/pub/software/scm/git/) | -      | -      | -      |
| [PHP](http://php.net/)                              | -      | -      | -      |
| [PostgreSQL](http://www.postgresql.org/)            | -      | -      | -      |
| [rsync](https://download.samba.org/pub/rsync/)      | 3.2.3  | 3.2.3  | 3.2.3  |

* [MinGW-w64](http://sourceforge.net/projects/mingw-w64/) **OUTDATED** needed
  for [redmine#2932](https://dev.cfengine.com/issues/2932)
  * Requires change of buildslaves (autobuild)

Other dependencies (**find out why they are needed!**)

* autoconf 2.69
