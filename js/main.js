import React from 'react';
import ReactDOM from 'react-dom';
import ExampleWork from './example-work';

const myWork = [
  {
    'title': "Serverless Website",
    'href': "https://example.com",
    'desc': "This website is the end product of an ACloudGuru course to build a website to showcase one's work portfolio using serverless technology.  It uses AWS S3, Lambda, CloudFront, Route53 for hosting the website, Github, CodeBuild, Lambda to automate continuous building and deployment, uses ReactJS, Babel, webpack, jest to do modern javascript development, testing, packaing",
    'image': {
      'desc': "Serverless Portfolio",
      'src': "images/example2.png",
      'comment': "A Serverless Portfolio"
    }
  }
]

ReactDOM.render(<ExampleWork work={myWork}/>, document.getElementById('example-work'));
