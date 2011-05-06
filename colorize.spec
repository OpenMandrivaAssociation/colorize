Name:    	colorize
Version: 	0.3.4
Release: 	1
License: 	GPLv2+
Group:		Text tools
URL:		http://www.solbu.net/hoved/english/software.htm
Source0: 	http://www.solbu.net/progs/%{name}-%{version}.tar.gz
Summary: 	Colorized output from tail, like your logfiles.
BuildArch:      noarch

Requires: 	perl

%description
This is a perl script, made by Istvan Karaszi, to colorize' your logs.
You can use your own colors, you can simply modify your config file 
in your home directory ($HOME), or system-wide (/etc/colorizerc).

%prep
%setup -q

%install
install -m644 %{name}.1.gz -D %{buildroot}%{_mandir}/man1/%{name}.1.gz
install -m755 %{name} -D %{buildroot}%{_bindir}/%{name}
install -m644 %{name}rc -D %{buildroot}%{_sysconfdir}/%{name}rc

%files
%doc README THANKS TIPS TODO examples copyright changelog.gz
%{_bindir}/%{name}
%{_sysconfdir}/%{name}rc
%{_mandir}/man1/%{name}.1*
