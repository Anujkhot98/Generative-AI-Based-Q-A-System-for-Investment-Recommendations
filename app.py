from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSequence

app = FastAPI()

# Initialize the ChatGroq model with your API key
llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",  # Specify the desired model
    temperature=0.7,                       # Set the temperature for response variability
    groq_api_key="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",
    streaming=True  # Your Groq API key
)



@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # Receive message from the frontend
            user_message = await websocket.receive_text()
            

            prompt = ChatPromptTemplate.from_messages([
                ("system", "You are a helpful assistant."),
                ("human", "{user_message}")
            ])


            # Prepare the input for the chain
            input_data = {"user_message": user_message}

            chain = prompt | llm

            # Generate a response using the chain
            # response = chain.invoke(input_data)

            # Stream the response back to the frontend
            # await websocket.send_text(response.content) 


            ### to stream the response
            for chunk in chain.stream(input_data): 
                await websocket.send_text(chunk.content)
    except WebSocketDisconnect:
        print("Client disconnected")
