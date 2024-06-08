import streamlit as st
import requests
 
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

def query(payload, api_key):
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def summarize_text(text, api_key):
    words = text.split()[:250]
    truncated_text = ' '.join(words)
    
    response = query({"inputs": truncated_text}, api_key)
    if 'error' in response:
        return f"Error: {response['error']}"
    try:
        return response[0]['summary_text']
    except (KeyError, IndexError) as e:
        return f"Unexpected response format: {response}"

