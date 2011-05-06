Name:    	colorize
Version: 	0.3.4
Release: 	%mkrel 1
License: 	GPLv2+
Group:		Text tools
URL:		http://www.solbu.net/hoved/english/software.htm
Source0: 	http://www.solbu.net/progs/%{name}-%{version}.tar.gz
Summary: 	Colorized output from tail, like your logfiles.
BuildRoot:	%{_temppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch

Requires: 	perl

%description
This is a perl script, made by Istvan Karaszi, to colorize' your logs.
You can use your own colors, you can simply modify your config file 
in your home directory ($HOME), or system-wide (/etc/colorizerc).


%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}/examples
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}
install -p -m 0644 %{name}.1* $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m 0755 %{name} $RPM_BUILD_ROOT/%{_bindir}
install -p -m 0644 %{name}rc $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}rc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_sysconfdir}/%{name}rc
%{_mandir}/man1/%{name}.1*
%doc README THANKS TIPS TODO examples copyright changelog.gz

