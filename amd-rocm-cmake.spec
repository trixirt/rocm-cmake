%global commit0 07ec4c536108ae943e37985915ef279529ac693f
%global debug_package %{nil}
%global _name amd-rocm-cmake
%global rocm_path /opt/rocm
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global up_name rocm-cmake

%define patch_level 1

%bcond_with debug
%bcond_with static

%if %{without debug}
  %if %{without static}
    %global suf %{nil}
  %else
    %global suf -static
  %endif
%else
  %if %{without static}
    %global suf -debug
  %else
    %global suf -static-debug
  %endif
%endif

Name: %{_name}%{suf}

Version:        5.6.1
Release:        %{patch_level}.git%{?shortcommit0}%{?dist}
Summary:        TBD
License:        MIT

URL:            https://github.com/trixirt/%{up_name}
Source0:        %{url}/archive/%{commit0}/%{up_name}-%{shortcommit0}.tar.gz

BuildArch: noarch
BuildRequires:  cmake

%description
TBD

%package devel
Summary:        TBD

%description devel
%{summary}


%prep
%autosetup -p1 -n %{up_name}-%{commit0}


%build
%cmake 	-DCMAKE_INSTALL_PREFIX=%{rocm_path}
%cmake_build

%install
%cmake_install

%files devel
/opt/rocm

%changelog
* Sat Aug 05 2023 Tom Rix <trix@redhat.com>
- Stub something together
