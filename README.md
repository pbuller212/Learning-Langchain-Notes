# Learning Langchain

Notes from [this book](https://www.amazon.com/Learning-LangChain-Building-Applications-LangGraph/dp/1098167287/ref=sr_1_1?crid=OJKL6YHXF5&dib=eyJ2IjoiMSJ9.NABpFJrg-6-jP3ExltagIA.z9-TdlSP_-930hor7rJCTzjy7ZNxwszlm1YaPaMJ56w&dib_&tag=amzfinder-20&keywords=978-1-098-16728-8+isbn)

This is about using the [langchain library](https://github.com/langchain-ai/langchain) to pair LLM's with other sources of computation

__Fine-tuned LLMs__ are created by taking base LLMs and further training them on a proprietary dataset for a specific task - describe LLMs that are tuned by the developer for their specific task.

Adapting an existing LLM for your task is called __prompt engineering__.  The main task of the software engineer working with LLMs is to take an existing LLM and work out how to get it to accomplish the task you need for your application.

Types of prompts
* __Zero-Shot__ Prompting
  * Chain of thought - "Think step by step"
  * __RAG__ or Retreival-Augmented Generation
    * prepend `context:` to the prompt
  * Tool Calling
    * prepend with a list of `Tools:`
* __Few-shot__ prompting - "providing the LLM with examples of other questions and the correct
answers, which enables the LLM to learn how to perform a new task without going
through additional training or fine-tuning."
  * Static few-shot prompting
  * Dynamic few-shot prompting

## Chapter 1: LLM Fundamentals with LangChain

