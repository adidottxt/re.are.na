import React, { Component } from "react"

import '../css/Button.css'

class Button extends Component {
    render() {
      return (
        <div id='button-div'>
          <button id='button' onClick={this._refreshPage}>{this.props.text}</button>
        </div>
      )
    }

    _refreshPage() {
        console.log('clicked');
        window.location.reload();
    }
}

export default Button
