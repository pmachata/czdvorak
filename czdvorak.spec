Name:		czdvorak
Version:	0.1
Release:	1%{?dist}
Summary:	Dvorak programming keyboard for Czech users

Group:          User Interface/X
License:	Public Domain
Source0:	czdvorak
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	xkeyboard-config
BuildArch:      noarch

%define datadir_xkb_symbols %{_datadir}/X11/xkb/symbols/

%description

This package contains a modification of Programmer Dvorak (dvp) for
users that do light-weight Czech typing.  Czech letters with
diacritics are accessible through level 3 shift (such as is typically
available through AltGr).

%prep
:

%build
:

%install
install -d $RPM_BUILD_ROOT%{datadir_xkb_symbols}
install -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{datadir_xkb_symbols}

%clean
:

%files
%defattr(-,root,root,-)
%{datadir_xkb_symbols}/*

%changelog
* Mon Nov 15 2010 Petr Machata <pmachata@redhat.com> - 0.1-1
- Initial release.
