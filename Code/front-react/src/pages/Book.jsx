import React from "react"

import ModifyBookForm from "./ModifyBook"
import RemoveBookForm from "./removeBook"

export default function Book(){

    return (
        <div>
            <div>
            <h2>Modify Book</h2>
            <ModifyBookForm />
            </div>
            <div>
            <h2>Remove Book</h2>
            <RemoveBookForm />
            </div>
        </div>
    )
}