%global tarball xf86-input-void
%global moduledir %(pkg-config xorg-server --variable=moduledir )
%global driverdir %{moduledir}/input

Summary:   Xorg X11 void input driver
Name:      xorg-x11-drv-void
Version:   1.3.0
Release:   4%{?dist}
URL:       http://www.x.org
License:   MIT
Group:     User Interface/X Hardware Support
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:   ftp://ftp.x.org/pub/individual/driver/%{tarball}-%{version}.tar.bz2

ExcludeArch: s390 s390x

BuildRequires: xorg-x11-server-sdk >= 1.4.99.1
BuildRequires: xorg-x11-util-macros >= 1.3.0

Requires:  xorg-x11-server-Xorg >= 1.4.99.1

%description 
X.Org X11 void input driver.

%prep
%setup -q -n %{tarball}-%{version}

%build
%configure --disable-static
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING
%{driverdir}/void_drv.so
%{_mandir}/man4/void.4*

%changelog
* Wed Jan 06 2010 Peter Hutterer <peter.hutterer@redhat.com> 1.3.0-4
- Use global instead of define as per Packaging Guidelines 

* Wed Jan 06 2010 Peter Hutterer <peter.hutterer@redhat.com> 1.3.0-3
- Silence rpmlint tab/spaces warning.
- Move COPYING under defattr to ensure the right attributes.

* Fri Sep 11 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.3.0-2
- Require xorg-x11-util-macros 1.3.0

* Fri Sep 11 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.3.0-1
- void 1.3.0

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Adam Jackson <ajax@redhat.com> - 1.2.0-2.1
- ABI bump

* Mon Jun 22 2009 Peter Hutterer <peter.hutterer@redhat.com> - 1.2.0-2
- void-1.2.0-Adjust-for-ABI_XINPUT_VERSION-7.patch: cope with new input ABI.

* Wed Feb 25 2009 Peter Hutterer <peter.hutterer@redhat.com> - 1.2.0-1
- void 1.2.0

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.1.1-9
- Autorebuild for GCC 4.3

* Wed Jan 16 2008 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.1.1-8
- Don't own %%{mandir}.

* Tue Nov 13 2007 Adam Jackson <ajax@redhat.com> 1.1.1-7
- Require xserver 1.4.99.1

* Mon Sep 24 2007 Adam Jackson <ajax@redhat.com> 1.1.1-6
- xf86-input-void 1.1.1

* Thu Aug 23 2007 Adam Jackson <ajax@redhat.com> - 1.1.0-6
- Rebuild for ppc toolchain bug

* Mon Jun 18 2007 Adam Jackson <ajax@redhat.com> 1.1.0-5
- Update Requires and BuildRequires.  Disown the module directories.

* Fri Feb 16 2007 Adam Jackson <ajax@redhat.com> 1.1.0-4
- ExclusiveArch -> ExcludeArch

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - sh: line 0: fg: no job control
- rebuild

* Wed Jun 28 2006 Mike A. Harris <mharris@redhat.com> 1.1.0-3
- Remove system owned directories from file manifest.

* Tue Jun 13 2006 Adam Jackson <ajackson@redhat.com> 1.1.0-2
- Build on ppc64

* Sun Apr 09 2006 Adam Jackson <ajackson@redhat.com> 1.1.0-1
- Update to 1.1.0 from 7.1RC1.

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> 1.0.0.5-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> 1.0.0.5-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 1.0.0.5-1
- Updated xorg-x11-drv-void to version 1.0.0.5 from X11R7.0

* Tue Dec 20 2005 Mike A. Harris <mharris@redhat.com> 1.0.0.4-1
- Updated xorg-x11-drv-void to version 1.0.0.4 from X11R7 RC4
- Removed 'x' suffix from manpage dirs to match RC4 upstream.

* Wed Nov 16 2005 Mike A. Harris <mharris@redhat.com> 1.0.0.2-1
- Updated xorg-x11-drv-void to version 1.0.0.2 from X11R7 RC2

* Fri Nov 04 2005 Mike A. Harris <mharris@redhat.com> 1.0.0.1-1
- Updated xorg-x11-drv-void to version 1.0.0.1 from X11R7 RC1
- Fix *.la file removal.

* Fri Sep 02 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-0
- Initial spec file for void input driver generated automatically
  by my xorg-driverspecgen script.
