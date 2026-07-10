from typing import TypedDict, List, Annotated
import operator



class AgentState(TypedDict):
    """
    Represents the state of an agent in the system.
    """
    messages: Annotated[List[dict], operator.add]
    current_query: str
    documents:List[str]
    plan: List[str]
    status:str
    final_answer: str