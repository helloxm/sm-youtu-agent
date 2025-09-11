import asyncio

from utu.agents import SimpleAgent
from utu.config import ConfigLoader
from utu.utils import AgentsUtils

EXAMPLE_QUERY = (
    "当前文件夹下面的所有文件pdf文件，按要求提取和保存到相应文件里。传给document agent的文件路径必须是绝对路径。 如果document agent失败，直接提示失败，不用pypdf处理。"
)


config = ConfigLoader.load_agent_config("examples/gesp_exams_coding")
worker_agent = SimpleAgent(config=config)


async def main_gradio():
    async with worker_agent as agent:
        res = agent.run_streamed(EXAMPLE_QUERY)
        # async for event in res.stream_events():
        #     print(event)
        await AgentsUtils.print_stream_events(res.stream_events())
        print(f"Final output: {res.final_output}")


if __name__ == "__main__":
    asyncio.run(main_gradio())
