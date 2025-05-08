#!/bin/bash

# Clone the wiki repository
git clone https://github.com/isubroto/c.l.a.r.a.wiki.git

# Copy wiki files
cp c.l.a.r.a/wiki/* c.l.a.r.a.wiki/

# Navigate to wiki directory
cd c.l.a.r.a.wiki

# Add all files
git add .

# Commit changes
git commit -m "Update wiki documentation"

# Push changes
git push origin main

echo "Wiki setup complete!" 