Name:		extra-keyboards
Version:	0.7
Release:	1%{?dist}
Summary:	Extra keyboards for X server

Group:          User Interface/X
License:	Public Domain
Source0:	czdvorak
Source1:	typematrix
Source2:	mirror
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	xkeyboard-config
BuildArch:      noarch

%define datadir_xkb_symbols %{_datadir}/X11/xkb/symbols/

%description

This package contains a couple of keyboard modifiers for X server.

This includes modification of Programmer Dvorak (dvp) for users that
do light-weight Czech typing.  Czech letters with diacritics are
accessible through level 3 shift (such as is typically available
through AltGr).

Another set of two keyboards is for left-handed typing, such that the
right half of the keyboard is accessible via level 3 shift.  One is
for a fairly ordinary keyboard, and another specifically for Kinesis
Advantage.

%prep
:

%build
:

%install
install -d $RPM_BUILD_ROOT%{datadir_xkb_symbols}
for source in %{SOURCE0} %{SOURCE1} %{SOURCE2}; do
    install -m 644 $source $RPM_BUILD_ROOT%{datadir_xkb_symbols}
done

%files
%defattr(-,root,root,-)
%{datadir_xkb_symbols}/*

%changelog
* Sat Jun 21 2014 Petr Machata <pmachata@redhat.com> - 0.7-1
- Add a mirrored dvorak layout for Kinesis Advantage keyboard

* Tue Jun 19 2012 Petr Machata <pmachata@redhat.com> - 0.6-1
- Add a mirrored dvorak keyboard

* Sun Dec 11 2011 Petr Machata <pmachata@redhat.com> - 0.5-1
- Add dead_stroke to AltGr+minus, move dead_macron to
  AltGr+Shift+underscore

* Sun Dec 11 2011 Petr Machata <pmachata@redhat.com> - 0.4-1
- Add dead_horn to AltGr+h

* Sat Oct 29 2011 Petr Machata <pmachata@redhat.com> - 0.3-1
- Add dead_hook to AltGr+/ (mnemonic: the same key as "?")

* Tue Nov 23 2010 Petr Machata <pmachata@redhat.com> - 0.2-1
- Replace ecaron for eacute
- Add the keyswaps keyboard
- Rename the package to extra-keyboards

* Mon Nov 15 2010 Petr Machata <pmachata@redhat.com> - 0.1-1
- Initial release.
