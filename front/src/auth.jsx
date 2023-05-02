import { useLocation, Navigate } from "react-router-dom";

export const setToken = (token) => {
	localStorage.setItem("access_token", token); // make up your own token
};

export const setRole = (role) => {
	localStorage.setItem("role", role); // make up your own token
};

export const fetchToken = () => {
	return localStorage.getItem("access_token");
};

export const fetchRole = () => {
	return localStorage.getItem("role");
};

export function RequireToken({ children }) {
	let auth = fetchToken();
	let location = useLocation();

	if (!auth) {
		return <Navigate to="/" state={{ from: location }} />;
	}

	return children;
}

export function RequireRole({ children }) {
	let role = fetchRole();
	let location = useLocation();

	if (role === "Admin") {
		return children;
	}

	return <Navigate to="/" state={{ from: location }} />;
}

export function RequireTokenButton() {
	let auth = fetchToken();
	if (!auth) {
		return false;
	} else {
		return true;
	}
}

export function NotRequireTokenButton() {
	let auth = fetchToken();
	if (!auth) {
		return true;
	} else {
		return false;
	}
}

export function RequireRoleButton() {
	let role = fetchRole();
	if (role === "Admin") {
		return true;
	} else {
		return false;
	}
}

export function CustomerOnlyButton() {
	let role = fetchRole();
	if (role === "Customer") {
		return true;
	} else {
		return false;
	}
}
