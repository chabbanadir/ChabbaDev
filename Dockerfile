# Step 1: Use Node.js as the base image
FROM node:20

# Step 2: Set the working directory
WORKDIR /app

# Step 3: Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Step 4: Copy the rest of the project files
COPY . .

# Step 5: Build the project for production
RUN npm run build

# Step 6: Expose the port Astro will run on
EXPOSE 3000

# Step 7: Command to run the app
CMD ["npm", "run", "start" "--", "--host","0.0.0.0"]]
#CMD ["npm", "run","preview", "--", "--host", "0.0.0.0"]
