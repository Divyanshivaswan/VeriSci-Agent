import requests
import xml.etree.ElementTree as ET

class PubMedRetrievalEngine:
    """
    Handles live, dynamic literature retrieval from NCBI PubMed REST APIs 
    to feed real-world context into VeriSci verification workflows.
    """
    def __init__(self):
        self.base_search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        self.base_summary_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

    def fetch_live_literature(self, query: str, max_results: int = 2) -> list:
        try:
            search_params = {
                "db": "pubmed",
                "term": query,
                "retmax": max_results,
                "retmode": "json"
            }
            response = requests.get(self.base_search_url, params=search_params, timeout=5)
            if response.status_code != 200:
                return ["Live literature fetch unavailable (API timeout)."]

            data = response.json()
            id_list = data.get("esearchresult", {}).get("idlist", [])

            if not id_list:
                return [f"No matching prior art found on PubMed for query: '{query}'."]

            summary_params = {
                "db": "pubmed",
                "id": ",".join(id_list),
                "retmode": "json"
            }
            sum_response = requests.get(self.base_summary_url, params=summary_params, timeout=5)
            if sum_response.status_code != 200:
                return ["Retrieved PubMed IDs, but failed to load summary metadata."]

            sum_data = sum_response.json().get("result", {})
            retrieved_chunks = []
            
            for p_id in id_list:
                if p_id in sum_data:
                    title = sum_data[p_id].get("title", "No Title")
                    source = sum_data[p_id].get("source", "PubMed Journal")
                    pub_date = sum_data[p_id].get("pubdate", "Recent")
                    retrieved_chunks.append(f"[{source} ({pub_date})] {title}")

            return retrieved_chunks

        except Exception as e:
            return [f"Literature retrieval exception: {str(e)}"]
