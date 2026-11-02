Name:		python-pillow-heif
Version:	1.8.1
Release:	1
Summary:	HEIF and AVIF support for Pillow
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://github.com/bigcat88/pillow_heif
Source0:	https://files.pythonhosted.org/packages/source/p/pillow-heif/pillow_heif-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	pkgconfig(libheif)

%description
pillow-heif decodes and encodes HEIF and AVIF images through the
system libheif and registers a Pillow opener. Hermes uses it when a
vision tool opens a HEIC file.

%prep -a
# -Werror fails the extension build on newer clang warnings.
sed -i \
	-e 's/"-Werror", //g' \
	-e 's/, "-Werror"//g' \
	-e 's/"-Werror"//g' \
	setup.py

%files
%doc README.md CHANGELOG.md
%license LICENSE.txt
%{python_sitearch}/pillow_heif
%{python_sitearch}/_pillow_heif*.so
%{python_sitearch}/pillow_heif-%{version}.dist-info
