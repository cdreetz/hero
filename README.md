# HEROSTUFF

One of the few things I've seen in a while that I saw and immediately thought "yes"

- AI native
- Simple
- AI integrated thoroughly

1. Smaller object detection model for the live cam 
- Identify objects, capture image


2. Some ViT like BLIP-VQA or ViLT (or GPT-V) 
- "image"
- "What is the name, description, and condition of this product?"


2. * Some text-to-text for structured output (or GPT w/ JSON mode)
- "Review this product summary and output the following JSON:"

```
item = {
        "listing_title": "Apple Macbook Pro",
        "description": "Apple Macbook Pro in Silver",
        "condition": "Like new",
}
```


3. price = Stockx_lookup(item)


4. List item
Add couple pictures
Done





### Possible features
- sellers scan 4 items, list 1
- buyers "looking for item" post
- sellers are notified someone is looking for item we know they have

