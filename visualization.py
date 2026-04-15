import matplotlib.pyplot as plt

# Example: training loss
loss = [0.9, 0.7, 0.5, 0.3]

plt.plot(loss)
plt.title("Training Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.show()