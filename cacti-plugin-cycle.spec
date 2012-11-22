# TODO
# - bundles jquery v1.6.3
# - bundles jquery-autocomplete  1.1
%define		plugin	cycle
%define		php_min_version 5.2.0
%include	/usr/lib/rpm/macros.php
Summary:	Automatically cycle through cacti graphs
Name:		cacti-plugin-%{plugin}
Version:	2.3
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://docs.cacti.net/_media/plugin:%{plugin}-v%{version}-1.tgz
# Source0-md5:	0ced9905198288b142ed27bb83251264
URL:		http://docs.cacti.net/plugin:cycle
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.554
Requires:	cacti >= 0.8.7e-8
Requires:	cacti(pia) >= 2.0
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-date
Requires:	php-json
Requires:	php-pcre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		plugindir		%{cactidir}/plugins/%{plugin}

%description
This plugin allows you to automatically view the Cacti graphs one by
one after a specified time delay.

%prep
%setup -qc
mv %{plugin}/{LICENSE,README} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a %{plugin}/* $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{plugindir}
