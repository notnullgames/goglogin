use url::{ Url };
use std::collections::HashMap;
use std::process;

use wry::{
    application::{
        event::{ Event, WindowEvent },
        event_loop::{ ControlFlow, EventLoop },
        window::WindowBuilder,
    },
    webview::WebViewBuilder,
};

fn main() -> wry::Result<()> {
  let event_loop = EventLoop::new();
  let window = WindowBuilder::new()
    .with_title("Gog Login")
    .build(&event_loop)?;
  
  let webview = WebViewBuilder::new(window)?
    .with_url("https://auth.gog.com/auth?client_id=46899977096215655&redirect_uri=https%3A%2F%2Fembed.gog.com%2Fon_login_success%3Forigin%3Dclient&response_type=code&layout=client2")?
    .with_navigation_handler(move |uri: String| {
        let u = Url::parse(&uri).unwrap();
        let h: HashMap<_, _> = u.query_pairs().into_owned().collect();
        match h.get("code") {
            Some(i) => {
                println!("{}", i);
                process::exit(0);
            },
            _ => ()
        }

        true
    })
    .build()?;

  #[cfg(debug_assertions)]
  webview.open_devtools();

  event_loop.run(move |event, _, control_flow| {
    *control_flow = ControlFlow::Wait;

    match event {
      Event::WindowEvent {
        event: WindowEvent::CloseRequested,
        ..
      } => *control_flow = ControlFlow::Exit,
      _ => (),
    }
  });
}
