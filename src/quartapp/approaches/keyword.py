from langchain_core.documents import Document

from quartapp.approaches.base import ApproachesBase


class KeyWord(ApproachesBase):
    async def run(
        self, messages: list, temperature: float, limit: int, score_threshold: float
    ) -> tuple[list[Document], str]:
        if messages:
            query = messages[-1]["content"]
            keyword_response = self._data_collection.find({"$text": {"$search": query}}).limit(limit)
            documents_list: list[Document] = []
            if keyword_response:
                for document in keyword_response:
                    documents_list.append(
                        Document(page_content=document["textContent"], metadata={"source": document["source"]})
                    )
                return documents_list, documents_list[0].page_content
        return [], ""
