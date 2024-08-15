import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 8))

# Draw rectangles for each layer
# User Interface
ax.add_patch(patches.Rectangle((0.3, 0.85), 0.4, 0.1, edgecolor='black', facecolor='lightblue'))
ax.text(0.5, 0.9, 'User Interface (UI)', horizontalalignment='center', verticalalignment='center', fontsize=12, fontweight='bold')

# Application Layer
ax.add_patch(patches.Rectangle((0.2, 0.65), 0.6, 0.2, edgecolor='black', facecolor='lightgreen'))
ax.text(0.5, 0.75, 'Application Layer', horizontalalignment='center', verticalalignment='center', fontsize=12, fontweight='bold')

# Data Layer
ax.add_patch(patches.Rectangle((0.15, 0.45), 0.7, 0.15, edgecolor='black', facecolor='lightyellow'))
ax.text(0.5, 0.525, 'Data Layer', horizontalalignment='center', verticalalignment='center', fontsize=12, fontweight='bold')

# Integration Layer
ax.add_patch(patches.Rectangle((0.1, 0.3), 0.8, 0.1, edgecolor='black', facecolor='lightcoral'))
ax.text(0.5, 0.35, 'Integration Layer', horizontalalignment='center', verticalalignment='center', fontsize=12, fontweight='bold')

# Database
ax.add_patch(patches.Rectangle((0.05, 0.15), 0.9, 0.1, edgecolor='black', facecolor='lightgray'))
ax.text(0.5, 0.2, 'Database', horizontalalignment='center', verticalalignment='center', fontsize=12, fontweight='bold')

# External Services
ax.add_patch(patches.Rectangle((0.05, 0.05), 0.9, 0.05, edgecolor='black', facecolor='white'))
ax.text(0.5, 0.075, 'External Services', horizontalalignment='center', verticalalignment='center', fontsize=12, fontweight='bold')

# Add text for components inside each layer
# UI Components
ax.text(0.5, 0.87, 'Developer Dashboard\nTeam Overview', horizontalalignment='center', verticalalignment='center', fontsize=10)

# Application Layer Components
ax.text(0.5, 0.7, 'Developer Network Analysis Module\nKnowledge Management Module\nRisk Management Module', 
        horizontalalignment='center', verticalalignment='center', fontsize=10)

# Data Layer Components
ax.text(0.5, 0.475, 'Developer Repository\nProject Repository\nKnowledge Base', 
        horizontalalignment='center', verticalalignment='center', fontsize=10)

# Integration Layer Components
ax.text(0.5, 0.325, 'Git Integration\nCommunication Tools Integration', 
        horizontalalignment='center', verticalalignment='center', fontsize=10)

# Database Components
ax.text(0.5, 0.175, 'Graph Database (Neo4j)\nRelational Database', 
        horizontalalignment='center', verticalalignment='center', fontsize=10)

# External Services Components
ax.text(0.5, 0.055, 'APIs for External Tools', horizontalalignment='center', verticalalignment='center', fontsize=10)

# Remove axes
ax.axis('off')

# Show the diagram
plt.show()
