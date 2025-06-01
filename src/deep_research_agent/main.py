import asyncio
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from dotenv import load_dotenv

from deep_research_agent.coordinator import ResearchCoordinator


console = Console()


async def main():
    console.print("[bold cyan]Welcome to the Deep Research Agent![/bold cyan]")
    console.print("This tool performs In-depth research on any topic using AI Agents.\n")
    
    query = Prompt.ask("[bold]What would you like to research?[/bold]")
    
    if not query.strip():
        console.print("[bold red]Error:[/bold red] Please provide a valid query.")
        return
    
    research_coordinator = ResearchCoordinator(query)
    report = await research_coordinator.research()




if __name__ == "__main__":
    asyncio.run(main())