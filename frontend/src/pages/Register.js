import { useState } from "react";
import API from "../api";
import "./Auth.css";

export default function Register() {
    const [form, setForm] = useState({
        username: "",
        email: "",
        password: "",
        role: "user",
    });

    const register = async () => {
        await API.post("/register", form);
        alert("Registered successfully");
        window.location = "/";
    };

    return (
        <div className="auth-bg">
            <div className="auth-card">
                <h2>GN TECH Trac</h2>
                <p className="subtitle">Create your account</p>

                <input
                    placeholder="Username"
                    onChange={(e) => setForm({ ...form, username: e.target.value })}
                />

                <input
                    type="email"
                    placeholder="Email"
                    onChange={(e) => setForm({ ...form, email: e.target.value })}
                />

                <input
                    type="password"
                    placeholder="Password"
                    onChange={(e) => setForm({ ...form, password: e.target.value })}
                />

                <select
                    onChange={(e) => setForm({ ...form, role: e.target.value })}
                >
                    <option value="user">User</option>
                    <option value="admin">Admin</option>
                </select>

                <button className="auth-btn" onClick={register}>
                    Register
                </button>

                <p className="link" onClick={() => (window.location = "/")}>
                    Already have an account? Login
                </p>
            </div>
        </div>
    );
}
