#!/bin/bash

# Initialize git repository if it doesn't exist
if [ ! -d "c.l.a.r.a.wiki/.git" ]; then
    cd c.l.a.r.a.wiki
    git init
    git remote add origin https://github.com/isubroto/c.l.a.r.a.wiki.git
    git checkout -b main
    cd ..
fi

# Navigate to wiki directory
cd c.l.a.r.a.wiki

# Add all files
git add .

# Commit changes
git commit -m "Update wiki documentation"

# Push changes
git push -u origin main

echo "Wiki pages pushed successfully!" 