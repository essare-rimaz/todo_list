from fastapi import Body

post_todo_example_1 = Body(
    examples=[
        {
        "name": "my_todo_item",
        "description": "just my description",
        "project_id": None
        }
    ],
)