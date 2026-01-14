import { useState } from "react";
import API from "../api";
import "./Auth.css";

export default function Login() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const login = async () => {
        const form = new FormData();
        form.append("username", email);
        form.append("password", password);

        const res = await API.post("/login", form);

        localStorage.setItem("token", res.data.access_token);

        const payload = JSON.parse(atob(res.data.access_token.split(".")[1]));
        localStorage.setItem("role", payload.role);

        window.location = "/products";
    };

    return (
        <div className="auth-bg">
            <div className="auth-card">
                <h2>GN TECH Trac</h2>
                <p className="subtitle">Login to your account</p>

                <input
                    type="email"
                    placeholder="Email"
                    onChange={(e) => setEmail(e.target.value)}
                />

                <input
                    type="password"
                    placeholder="Password"
                    onChange={(e) => setPassword(e.target.value)}
                />

                <button className="auth-btn" onClick={login}>
                    Login
                </button>

                <p className="link" onClick={() => (window.location = "/register")}>
                    Create new account
                </p>
            </div>
        </div>
    );
}
