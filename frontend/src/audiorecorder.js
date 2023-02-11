import React, { Component } from "react";
import AudioAnalyser from "react-audio-analyser";
import axios from "axios";


// import dotenv from 'dotenv';

// dotenv.config();

export default class AudioRecorder extends Component {
  constructor(props) {
    super(props);
    this.state = {
      status: "",
      response: "",
      blob: null,
      audioSrc: null
    };
  }

  async sendAudio1() {
      console.log("send",this.state.blob);
      const arrayBuffer = await this.state.blob.arrayBuffer();
    const data = {audioData:btoa(String.fromCharCode.apply(null, new Uint8Array(arrayBuffer)))};
    const config = {
            headers: {'content-type': 'application/json'}
            }
        console.log(JSON.stringify(data));
        // axios.post('http://localhost:5000/audio', data, config).then((resp)=>{console.log(resp.data.body)
        // this.setState({
            // response: resp.data.body
        //   }); console.log(this.state.response)}).catch((error)=>console.log(error))
        const result = await(await axios.post('http://localhost:5000/audio', data, config)).data
        this.setState({response:result.body})
        console.log(result.body)
        
  }

  controlAudio(status) {
    this.setState({
      status
    });
  }

  changeScheme(e) {
    this.setState({
      audioType: e.target.value
    });
  }

  componentDidMount() {
    this.setState({
      audioType: "audio/mp3"
    });
  }

  render() {
    const { status, audioSrc, blob } = this.state;
    const audioType = "audio/mp3";
    const audioProps = {
      audioType,
      // audioOptions: {sampleRate: 30000}, // 设置输出音频采样率
      status,
      audioSrc,
      blob,
      timeslice: 2000, // timeslice（https://developer.mozilla.org/en-US/docs/Web/API/MediaRecorder/start#Parameters）
      startCallback: (e) => {
        console.log("succ start", e);
      },
      stopCallback: (e) => {
        this.setState({
          audioSrc: window.URL.createObjectURL(e)
        });
        this.setState({ blob: e });
        console.log("succ stop", e);
      },
      onRecordCallback: (e) => {
        console.log("recording", e);
      },
      errorCallback: (err) => {
        console.log("error", err);
      }
    };
    return (
      <div>
        <AudioAnalyser {...audioProps}>
          <div className="btn-box">
            <button
              className="btn"
              onClick={() => this.controlAudio("recording")}
            >
              Start
            </button>
            <button
              className="btn"
              onClick={() => this.controlAudio("inactive")}
            >
              Stop
            </button>
            <button className="btn" onClick={async() => await this.sendAudio1()}>
              send
            </button>
          </div>
          <h1>Réponse : {this.state.response}</h1>
        {/* <p>{this.state.response}</p> */}
        </AudioAnalyser>
      </div>
    );
  }
}