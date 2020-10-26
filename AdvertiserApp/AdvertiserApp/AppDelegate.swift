//
//  AppDelegate.swift
//  AdvertiserApp
//
//  Created by PubMatic on 18/10/20.
//

import UIKit
import StoreKit

@main
class AppDelegate: UIResponder, UIApplicationDelegate {



    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        // Override point for customization after application launch.
        
        // Apps that are advertised by an ad network campaign call registerAppForAdNetworkAttribution() method or updateConversionValue(_:) when the app first launches. Both methods generate an install notification, which is the cryptographically signed data that validates that a user installed and launched this app as a result of an ad.
        
        // The first call to registerAppForAdNetworkAttribution() generates the notification if the device has attribution data for that app, and starts a 24-hour timer. Subsequent calls to this method have no effect. You may, however, call updateConversionValue(_:) to provide a conversion value and restart the timer.
        
        // The device sends the install notification to the ad network’s postback URL within 0-24 hours after the timer expires. Ad networks must verify the postback after receiving it..

        SKAdNetwork.registerAppForAdNetworkAttribution()
        
        return true
    }

    // MARK: UISceneSession Lifecycle

    func application(_ application: UIApplication, configurationForConnecting connectingSceneSession: UISceneSession, options: UIScene.ConnectionOptions) -> UISceneConfiguration {
        // Called when a new scene session is being created.
        // Use this method to select a configuration to create the new scene with.
        return UISceneConfiguration(name: "Default Configuration", sessionRole: connectingSceneSession.role)
    }

    func application(_ application: UIApplication, didDiscardSceneSessions sceneSessions: Set<UISceneSession>) {
        // Called when the user discards a scene session.
        // If any sessions were discarded while the application was not running, this will be called shortly after application:didFinishLaunchingWithOptions.
        // Use this method to release any resources that were specific to the discarded scenes, as they will not return.
    }


}

