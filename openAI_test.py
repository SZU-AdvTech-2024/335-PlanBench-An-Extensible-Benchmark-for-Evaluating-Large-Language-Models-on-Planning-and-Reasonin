import os

import openai


def query_gpt4(question):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    #openai.base_url = url
    openai.base_url = os.getenv('OPENAI_API_BASE')

    try:
        response = openai.chat.completions.create(
            model="gemini-pro",  # 确认使用 gpt-4o 模型
            messages=[
                {"role": "system", "content": "You are the planner assistant who comes up with correct plans."},
                {"role": "user", "content": question},
            ],
            temperature=0,
        )
        print(response)
        return response.choices[0].message.content
    except Exception as e:
        return str(e)

# 问题
question = "为什么太阳那么红？"

query = "I am playing with a set of blocks where I need to arrange the blocks into stacks. Here are the actions I can do\n\nPick up a block\nUnstack a block from on top of another block\nPut down a block\nStack a block on top of another block\n\nI have the following restrictions on my actions:\nI can only pick up or unstack one block at a time.\nI can only pick up or unstack a block if my hand is empty.\nI can only pick up a block if the block is on the table and the block is clear. A block is clear if the block has no other blocks on top of it and if the block is not picked up.\nI can only unstack a block from on top of another block if the block I am unstacking was really on top of the other block.\nI can only unstack a block from on top of another block if the block I am unstacking is clear.\nOnce I pick up or unstack a block, I am holding the block.\nI can only put down a block that I am holding.\nI can only stack a block on top of another block if I am holding the block being stacked.\nI can only stack a block on top of another block if the block onto which I am stacking the block is clear.\nOnce I put down or stack a block, my hand becomes empty.\nOnce you stack a block on top of a second block, the second block is no longer clear.\n\n[STATEMENT]\nAs initial conditions I have that, the blue block is clear, the orange block is clear, the hand is empty, the orange block is on top of the yellow block, the yellow block is on top of the red block, the red block is on the table and the blue block is on the table.\nMy goal is to have that the red block is on top of the orange block, the blue block is on top of the red block and the yellow block is on top of the blue block.\n\nMy plan is as follows:\n\n[PLAN]\n1. \n   - Reasoning: To move the yellow block, the orange block must be removed first.\n   - Action: Unstack the orange block from on top of the yellow block.\n2.\n   - Reasoning: Placing the orange block on the table clears the way to handle the yellow block.\n   - Action: Put down the orange block.\n3.\n   - Reasoning: To move the red block, the yellow block must be removed first.\n   - Action: Unstack the yellow block from on top of the red block.\n4.\n   - Reasoning: Placing the yellow block on the table allows access to the red block.\n   - Action: Put down the yellow block.\n5.\n   - Reasoning: To place the red block on the orange block as per the goal.\n   - Action: Pick up the red block.\n6.\n   - Reasoning: This achieves part of the desired final arrangement.\n   - Action: Stack the red block on top of the orange block.\n7.\n   - Reasoning: To place it on top of the red block as per the goal.\n   - Action: Pick up the blue block.\n8.\n   - Reasoning: This sets up the final position for the yellow block.\n   - Action: Stack the blue block on top of the red block.\n9.\n   - Reasoning: To complete the goal by placing it on top of the blue block.\n   - Action: Pick up the yellow block.\n10.\n    - Reasoning: This completes the desired final arrangement.\n    - Action: Stack the yellow block on top of the blue block.\n\n[PLAN END]\n\n[STATEMENT]\nAs initial conditions I have that, the red block is clear, the blue block is clear, the yellow block is clear, the hand is empty, the blue block is on top of the orange block, the red block is on the table, the orange block is on the table and the yellow block is on the table.\nMy goal is to have that the orange block is on top of the blue block.\n\nMy plan is as follows:\n\n[PLAN]\nunstack the blue block from on top of the orange block\nput down the blue block\npick up the orange block\nstack the orange block on top of the blue block\n[PLAN END]\n\n[STATEMENT]\nAs initial conditions I have that, the red block is clear, the yellow block is clear, the hand is empty, the red block is on top of the blue block, the yellow block is on top of the orange block, the blue block is on the table and the orange block is on the table.\nMy goal is to have that the orange block is on top of the red block.\n\nMy plan is as follows:\n\n[PLAN]",

# 获取并打印回答
answer = query_gpt4(question)
print(answer)