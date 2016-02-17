Name:		proprietary-fonts
Version:	0.0
Release:	1.R
Summary:	Some Proprietary fonts Collection

License:	Proprietary
URL:		https://thepiratebay.se/
Source0:	proprietary-fonts-0.0.tar.xz
	

BuildRequires:	fontpackages-devel
Requires:	fontpackages-filesystem

BuildArch:	noarch


%description
This package provides Consolas, Menlo, Monaco, SFUIText, San Francisco
fonts.


%prep
%setup -q


%build


%install
install -d %{buildroot}/%{_fontdir}
install -m 644 *.ttf %{buildroot}/%{_fontdir}

%_font_pkg *.ttf

%license LICENSE

%changelog
* Wed Feb 17 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 0.0-1.R
- initial build
