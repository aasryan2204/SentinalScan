from rich.console import Console

console = Console()


def display_banner():
    console.print(
        """
[bold cyan]
=================================================
                SentinelScan v0.1.0
        Python Network Reconnaissance Tool
=================================================
[/bold cyan]
"""
    )


def main():
    display_banner()


if __name__ == "__main__":
    main()