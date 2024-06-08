import streamlit as st
import search
import summary

def main():
    st.title("Perplex Search")

    search_query = st.text_input("Enter your search query:")
    api_key = st.text_input("Enter your Hugging Face API Key:", type="password")

    if st.button("Search"):
        if search_query and api_key:
            with st.spinner("Scraping Bing search results..."):
                links = search.scrape_bing(search_query)
            
            combined_text = ""
            with st.spinner("Fetching content from links..."):
                for link in links:
                    content = search.fetch_content(link)
                    combined_text += content + " "

            if combined_text.strip():
                with st.spinner("Summarizing the text..."):
                    summary_text = summary.summarize_text(combined_text, api_key)
                st.subheader("Summary")
                st.write(summary_text)
            else:
                st.error("Failed to fetch content from the links.")
        else:
            st.error("Please enter a search query and your Hugging Face API Key.")

if __name__ == "__main__":
    main()
