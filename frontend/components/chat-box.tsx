"use client";

import { useState } from "react";

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

export default function ChatBox() {
  const [message, setMessage] = useState("");
  const [reply, setReply] = useState("");
  const [loading, setLoading] = useState(false);

  async function sendMessage() {
    if (!message.trim() || loading) return;
    setLoading(true);
    setReply("");
    try {
      const res = await fetch(`${API_BASE_URL}/api/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message }),
      });
      const data = await res.json().catch(() => ({}));

      if (!res.ok) {
        setReply(
          typeof data.detail === "string"
            ? data.detail
            : "Something went wrong. Please check your message and try again."
        );
        return;
      }
      setReply(data.reply);
    } catch {
      setReply("Could not reach the backend. Is it running?");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div style={{ marginTop: 24 }}>
      <input
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && sendMessage()}
        placeholder="Ask IntelliDesk something..."
        style={{ padding: 8, width: 300 }}
      />
      <button onClick={sendMessage} disabled={loading} style={{ marginLeft: 8, padding: 8 }}>
        {loading ? "Thinking..." : "Send"}
      </button>
      {reply && <p style={{ marginTop: 12 }}>{reply}</p>}
    </div>
  );
}