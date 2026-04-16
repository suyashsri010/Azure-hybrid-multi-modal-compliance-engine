import operator
from typing import Annotated, List, Dict, Optional, Any, TypedDict

# defining schema for a single compliance result
# error report
class ComplianceIssue(TypedDict):
    category: str
    description: str # specific detail of violation
    severity: str # critical or warning
    timestamp: Optional[str]

# define the global graph state
# this defines the state that gets passed around in the agentic workflow
class VideoAuditState(TypedDict):
    '''
    Defines the data schema for langgraph execution content
    Main Container : holds all the information about the audit
    right from the initial URL to the final report
    '''
    #input parameters
    video_url :str
    video_id :str

    #ingestion and extracted data
    local_file_path:Optional[str]
    video_metadata:Dict[str,Any] # {"duration":15,"resolution":"1080p"}
    transcript:Optional[str] # Fully extracted speech to text

    #analysis output
    #stores the list of all the violations found by AI
    compliance_results : Annotated[List[ComplianceIssue],operator.add]

    #final deliverables:
    final_status : str # PASS | FAIL
    final_report : str # markdown format

    #System observability
    #errors: API timeout, system level errors
    #stores the list of system level crashes
    errors : Annotated[List[str],operator.add]

