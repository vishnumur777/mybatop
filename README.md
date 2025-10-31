
<h1 align="center"><b>mybatop</b></h1>
<h3 align="center">A diagnostic reporting tool specially made for batteries in linux laptops.</h3>

<p align="center">
    <img src="https://github.com/vishnumur777/mybatop/actions/workflows/build-packages.yml/badge.svg" alt="Build Packages workflow">
    <img src="https://github.com/vishnumur777/mybatop/actions/workflows/lint-bash.yml/badge.svg" alt="Bash Linting workflow">
    <img src="https://github.com/vishnumur777/mybatop/actions/workflows/push-aur.yml/badge.svg" alt="AUR push">
    <img src="https://github.com/vishnumur777/mybatop/actions/workflows/push-fedora-copr.yml/badge.svg" alt="Fedora COPR">
    <img src="https://github.com/vishnumur777/mybatop/actions/workflows/test-python.yml/badge.svg" alt="Python unit testing">
    <img src="https://img.shields.io/github/license/vishnumur777/mybatop" alt="License">
    <img src="https://img.shields.io/github/forks/vishnumur777/mybatop" alt="GitHub forks">
    <img src="https://img.shields.io/github/stars/vishnumur777/mybatop" alt="GitHub Repo stars">
    <img src="https://img.shields.io/github/issues/vishnumur777/mybatop" alt="GitHub Issues">
    <img src="https://img.shields.io/github/issues-pr/vishnumur777/mybatop" alt="GitHub Pull Requests">
</p>

<p align="center">
  <img src="logo.svg" alt="mybatop" width="500px" height="500px"/>
</p>

<!-- <p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/3582/3582038.png" alt="mybatop custom image" />
</p> -->

#### **mybatop is a command-line utility designed for Linux systems, inspired from powercfg for windows and lshw utility.**



## ✨ Features

- **🔋 Comprehensive Battery Monitoring**: Real-time tracking of battery status, capacity, voltage, current, and charge cycles with automatic background logging

- **📊 Multiple Report Formats**: Generate detailed reports in HTML (with interactive charts), JSON, XML, and CSV formats with flexible export options

- **📈 Visual Analytics Dashboard**: Interactive Plotly graphs showing battery health trends, capacity history, cycle counts, and usage patterns since installation

- **⚡ Intelligent State Tracking**: Automatic detection and logging of power states (active/low-power/suspended) and system events (startup/shutdown/lid actions)

- **🎯 Detailed Usage Insights**: Comprehensive metrics including recent usage (3 days), technical specifications, monthly capacity averages, and activity timelines

- **🛠️ Easy CLI Integration**: Simple command-line interface with systemd service integration for effortless monitoring without manual intervention




## ⚙️ Installation
   


Installation of mybatop is simple and easy. We can download mybatop on 3 different distros.

- Ubuntu/Debian
- Fedora/OpenSUSE/CentOS
- Arch Linux

### 1. Ubuntu/Debian

1. Download latest version of mybatop in [Downloads](https://mybatop.web.app/download) page.
2. Open terminal and navigate to the directory where the downloaded file is located.
3. Run the following command to install mybatop.

```bash
sudo dpkg -i mybatop-*.deb
```

### 2. Fedora/OpenSUSE/CentOS

1. Run the following command to install mybatop using `dnf` package manager.

```bash
sudo dnf copr enable vishnumur777/mybatop
sudo dnf install mybatop-*.rpm
```

(OR)


1. Download latest version of mybatop in [Downloads](https://mybatop.web.app/download) page.
2. Open terminal and navigate to the directory where the downloaded file is located.
3. Run the following command to install mybatop.

```bash
sudo rpm -i mybatop-*.rpm
```

### 3. Arch Linux

1. Run the following command to install mybatop using `yay` package manager.

```bash
yay -S mybatop
```

(OR)

1. Download latest version of mybatop in [Downloads](https://mybatop.web.app/download) page.
2. Open terminal and navigate to the directory where the downloaded file is located.
3. Run the following command to install mybatop.

```bash
sudo pacman -U mybatop-*.pkg.tar.xz
```

## 🛠️ Usage

```bash
mybatop <OPTIONS> <TAG>
```

### List of Options

- report
- data
- help

**Example:**

### `help` Command

```bash
mybatop --help
```

#### 1. Diagnosed HTML Report 📊✨

```bash
mybatop report --html
```
> **Note: same for getting reports other formats (JSON, XML). Use `--json`, `--xml`.**

#### 2. Getting data in CSV 📄✨

```bash
mybatop data --csv
```

> **Note: same for getting data other formats (JSON, XML). Use `--json`, `--xml`.**

### Classes in Report Generation 📊✨

**Usage:**

```bash
mybatop report -C <CLASS-TYPE> <TAG>
```

#### List of Classes

- recent-usage
- tech-spec
- average-capacity
- batcaphis
- cycle-count
- battery-health
- batuseact

**Example:**

```bash
mybatop report -C recent-usage --html
```

> **Note: same for getting reports in other classes in other formats (JSON, XML, CSV). Use `--json`, `--xml`, `--csv`.**

Refer all other commands [here](https://mybatop.web.app/docs/gen-reports#generate-report-with-classes)
## Contributions

- All contributors are welcome to contribute.
- Contributing guidelines are present under [CONTRIBUTING.md](CONTRIBUTING.md)
- Beginners are open to contribute under **good first issues**.

## Contributors ✨
<a href="https://github.com/vishnumur777/mybatop/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=vishnumur777/mybatop" />
</a>

## License

This project is licensed under the terms of [GPL-3.0 License](LICENSE)
