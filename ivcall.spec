Summary:	A Linux tool for doing automated ISDN voice calls
Summary(pl):	Linuksowe narzêdzie do automatycznego wykonywania po³±czeñ g³osowych ISDN
Name:		ivcall
Version:	0.4
Release:	0.1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://freshmeat.net/redir/ivcall/4638/url_tgz/%{name}-%{version}.tar.gz
# Source0-md5:	643619c81f83ba0a05aa2497ce12c035
URL:		http://0pointer.de/lennart/projects/ivcall/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ivcall is a small utility which may be used to make automated
telephone calls with your isdn4linux supported ISDN card. Outgoing
calls are supported as well as incoming calls. The audio data received
from the peer is written to STDOUT, audio data read from STDIN is send
to the peer. The audio data is in raw 8 bit uLaw 8 kHz format, without
any headers.

%description -l pl
ivcall to ma³e narzêdzie do automatycznego wykonywania po³±czeñ
telefonicznych przy u¿yciu kart ISDN obs³ugiwanych przez isdn4linux.
Obs³ugiwane s± po³±czenia wychodz±ce jak i przychodz±ce. Dane g³osowe
odbierane od drugiej strony s± wysy³ane na standardowe wyj¶cie, a dane
g³osowe odczytywane ze standardowego wyj¶cia s± wysy³ane do drugiej
strony. Dane d¼wiêkowe s± w formacie surowym 8-bitowym uLaw 8kHz, bez
¿adnych nag³ówków.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/ivcall.1*
