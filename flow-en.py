"""
 ライブ参加者が報酬を受け取るために必要な認証を得るための手順をフローチャートとして出力します。
 出力形式はPNGやPDFなどを指定できます。
"""

from graphviz import Digraph

# Create a graph object:
dot = Digraph(format="png", comment="Send NEM Flow")

# Add nodes:
dot.node("start")
dot.node("nw", "NEMber Wallet")
dot.node("dw", "DJ Wallet")
dot.node("judge", shape="diamond")
dot.node("end")

# Add edges:
dot.edge("start", "nw", label="")
dot.edge("nw", "dw", label="1. send 0 NEM", headport="w")
dot.edge("dw", "nw", label="2. 2 question\n   with ENC")
dot.edge("nw", "dw", label="3. answer\n   with ENC", headport="e")
dot.edge("dw", "judge", label="4. judgement", headport="n")
dot.edge("judge", "nw", label="5. ok!\n  rewards", tailport="e")
dot.edge("judge", "end", label=" 6. done")


# Check the generated source code:
print(dot.source)

# Save and render the source code, optionally view the result:
dot.render("dist/djflow", view=False)
